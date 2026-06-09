# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 15:00:05 EDT`
Last processed slot: `entry_1500`

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
- Equity: `$30,952.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$730.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   0     73     14965.0                 15695.0         2.05           2.15       52.68         52.72          bid_ask_mid                       2.15                bid_ask_mid                    True           730.0                   4.88         93.55               31              0.59         45.34           45.61                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           83.33               18            1.86              1.09         82.71                69.62         0.651          pass              0.207              0.0                           0.167               -2.50             -0.145                                 ok            True                  False
  CTSH           93.55               31            0.51              0.19         52.91                51.28         0.581          pass              0.770             70.3                           0.525                1.76             -0.104                                 ok            True                  False
   WMT           81.82               22            1.00              0.84        119.47                36.35         0.562          pass              0.288             34.4                           0.441                0.05              0.090                                 ok            True                  False
  TEAM           96.15               26            2.79              1.91         97.07                87.01         0.552          pass              0.723             53.6                           0.613               12.05              0.809                                 ok            True                  False
  CDNS           94.29               35            0.67              1.86        393.44                58.79         0.517          pass              0.853             84.5                           0.756                2.58              0.480                                 ok            True                   True
    ZS           71.43               14            3.50              3.16        127.89               157.94         0.845          pass              0.250             46.2                           0.602              -32.43             -1.879            downtrend_blocked_slope           False                  False
  DRAM          100.00               14            2.10              0.89         60.14               103.58         0.685          pass              0.720             75.0                           0.599               -2.08             -0.328            downtrend_blocked_slope           False                  False
  INTU           61.54               13            4.08              8.73        301.77               100.92         0.620          pass              0.121             13.0                           0.239               -3.72             -0.629 downtrend_blocked_slope_and_streak           False                  False
  CSCO          100.00                3            3.26              2.83        122.94                58.94         0.608          pass              0.589             42.6                           0.580                1.50              0.446                                 ok           False                  False
  MSFT           83.33                6            1.96              5.64        409.32                36.13         0.603          pass              0.267             39.2                           0.491               -2.97             -0.372            downtrend_blocked_slope           False                  False
  AVGO           88.89               27            1.23              3.41        395.14                69.53         0.561          pass              0.651             81.5                           0.840               -7.18             -0.917            downtrend_blocked_slope           False                  False
  PANW           78.57               14            2.58              4.82        264.27                58.75         0.546          pass              0.245             54.5                           0.701                1.05              0.368                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-09T15:00:05.106979-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T14:55:02.051864-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-09T14:50:06.133016-04:00       entry_1500                   entry {"allocated_cash": 14965.0, "asset_type": "option", "contract_symbol": "CTSH260717C00055000", "contracts": 73, "early_entry_score": 0.757, "entry_mode": "regular", "entry_option_price": 2.05, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1420.0, "option_spread_pct": 9.76, "option_volume": 78.0, "success_rate": 93.55, "ticker": "CTSH", "timing_score": 0.576}
2026-06-09T14:50:06.133016-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                             {"early_entry_score": 0.238, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 12.77, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.669}
2026-06-09T14:50:06.133016-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-09", "training_samples": 5214, "window": 5}
2026-06-09T12:00:03.055569-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:55:04.019844-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:50:02.014967-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:45:02.008648-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:40:06.401362-04:00 early_entry_1140      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609150005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609150005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609150005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609150005)

</details>
