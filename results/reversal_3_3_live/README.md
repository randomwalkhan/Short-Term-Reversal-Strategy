# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 15:45:06 EDT`
Last processed slot: `manual`

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
  CTSH     option         option CTSH260717C00055000       2026-06-09                   0     73     14965.0                 16060.0         2.05            2.2       52.68         52.86          bid_ask_mid                        2.2                bid_ask_mid                    True          1095.0                   7.32         93.55               31              0.59         45.34           45.75                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           86.36               22            0.84              0.49         82.97                69.62         0.690          pass              0.483             54.8                           0.614               -1.48             -0.098                                 ok            True                  False
   WMT           80.95               21            1.06              0.89        119.45                36.35         0.564          pass              0.247             30.6                           0.268               -0.01              0.087                                 ok            True                  False
  TEAM           96.15               26            2.76              1.89         97.08                87.01         0.555          pass              0.725             54.2                           0.624               12.09              0.810                                 ok            True                  False
  CDNS           92.31               26            1.25              3.44        392.77                58.79         0.540          pass              0.703             71.3                           0.443                1.99              0.454                                 ok            True                  False
  WDAY           83.33               24            2.29              2.30        142.77                70.13         0.514          pass              0.423             63.0                           0.788               13.26              1.333                                 ok            True                  False
    ZS           71.43               14            3.41              3.08        127.93               157.94         0.848          pass              0.254             47.6                           0.621              -32.37             -1.875            downtrend_blocked_slope           False                  False
  DRAM          100.00               14            2.33              0.99         60.10               103.58         0.671          pass              0.710             72.2                           0.691               -2.31             -0.339            downtrend_blocked_slope           False                  False
  INTU           61.54               13            4.03              8.62        301.81               100.92         0.623          pass              0.124             14.0                           0.349               -3.67             -0.627 downtrend_blocked_slope_and_streak           False                  False
  CSCO          100.00                1            3.51              3.05        122.84                58.94         0.607          pass              0.575             38.2                           0.453                1.23              0.435                                 ok           False                  False
  MSFT           75.00                4            2.31              6.65        408.89                36.13         0.583          pass              0.143             28.3                           0.250               -3.32             -0.388            downtrend_blocked_slope           False                  False
  CTSH           94.59               37            0.25              0.09         52.95                51.28         0.557          pass              0.880             85.2                           0.673                2.02             -0.092                                 ok           False                  False
  AVGO           86.36               22            1.77              4.90        394.50                69.53         0.555          pass              0.525             73.4                           0.639               -7.68             -0.942            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609154506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609154506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609154506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609154506)

</details>
