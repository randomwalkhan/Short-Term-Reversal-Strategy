# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 15:30:02 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$15,257.25`
- Equity: `$31,317.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$1,095.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   0     73     14965.0                 16060.0         2.05            2.2       52.68         52.79          bid_ask_mid                        2.2                bid_ask_mid                    True          1095.0                   7.32         93.55               31              0.59         45.34           46.02                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           83.33               18            1.36              0.79         82.84                69.62         0.681          pass              0.292             27.1                           0.496               -1.99             -0.122                                 ok            True                  False
   WMT           80.95               21            1.08              0.90        119.44                36.35         0.563          pass              0.244             29.5                           0.375               -0.03              0.087                                 ok            True                  False
  TEAM           96.15               26            2.87              1.97         97.05                87.01         0.547          pass              0.718             52.3                           0.518               11.96              0.805                                 ok            True                  False
  CDNS           93.10               29            1.13              3.12        392.90                58.79         0.527          pass              0.751             74.0                           0.463                2.10              0.459                                 ok            True                  False
  WDAY           81.82               22            2.60              2.62        142.64                70.13         0.505          pass              0.353             58.0                           0.773               12.90              1.318                                 ok            True                  False
  AMGN           88.00               25            0.73              1.78        344.97                22.55         0.502          pass              0.419             18.3                           0.126                2.16              0.376                                 ok            True                  False
    ZS           76.92               13            3.84              3.48        127.76               157.94         0.840          pass              0.227             40.9                           0.370              -32.67             -1.895            downtrend_blocked_slope           False                  False
  DRAM          100.00               11            2.73              1.16         60.02               103.58         0.665          pass              0.676             67.5                           0.465               -2.71             -0.357            downtrend_blocked_slope           False                  False
  INTU           64.29               14            4.01              8.58        301.83               100.92         0.621          pass              0.132             14.4                           0.376               -3.65             -0.626 downtrend_blocked_slope_and_streak           False                  False
  MSFT           75.00                4            2.30              6.64        408.89                36.13         0.583          pass              0.144             28.4                           0.304               -3.31             -0.388            downtrend_blocked_slope           False                  False
   CEG           78.95               38            0.05              0.08        250.63                55.25         0.579          pass              0.538             97.7                           0.657              -16.92             -1.821 downtrend_blocked_slope_and_streak           False                  False
  CTSH           94.44               36            0.29              0.11         52.94                51.28         0.561          pass              0.864             83.0                           0.594                1.98             -0.094                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-09T15:10:01.102188-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T15:05:03.068175-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T15:00:05.106979-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T14:55:02.051864-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T14:50:06.133016-04:00       entry_1500                   entry {"allocated_cash": 14965.0, "asset_type": "option", "contract_symbol": "CTSH260717C00055000", "contracts": 73, "early_entry_score": 0.757, "entry_mode": "regular", "entry_option_price": 2.05, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1420.0, "option_spread_pct": 9.76, "option_volume": 78.0, "success_rate": 93.55, "ticker": "CTSH", "timing_score": 0.576}
2026-06-09T14:50:06.133016-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                             {"early_entry_score": 0.238, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 12.77, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.669}
2026-06-09T14:50:06.133016-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-09", "training_samples": 5214, "window": 5}
2026-06-09T12:00:03.055569-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:55:04.019844-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:50:02.014967-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609153002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609153002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609153002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609153002)

</details>
