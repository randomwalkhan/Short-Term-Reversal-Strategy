# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 15:15:10 EDT`
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

- Cash: `$14,720.50`
- Equity: `$28,160.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-1,200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   2     32     14640.0                 13440.0         4.58            4.2      126.19        125.34          bid_ask_mid                        4.2                bid_ask_mid                    True         -1200.0                   -8.2         93.33               15              1.32         33.41           33.41                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-07-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               11            0.93              0.52         80.08                19.51         0.613          pass              0.538             23.5                           0.314                0.72              0.413                                 ok            True                  False
   EXC           84.62               13            0.89              0.29         46.50                18.60         0.587          pass              0.275             24.5                           0.448               -0.83              0.184                                 ok            True                  False
   AEP           81.82               11            1.22              1.17        136.31                19.16         0.560          pass              0.181             23.4                           0.367                4.15              0.766                                 ok            True                  False
  GILD           85.00               20            0.84              0.74        126.02                28.09         0.546          pass              0.292             12.4                           0.191               -1.53              0.046                                 ok            True                  False
  AMGN           93.10               29            0.67              1.69        361.40                26.93         0.516          pass              0.657             43.0                           0.362                3.41              0.629                                 ok            True                  False
  AVGO           77.27               22            1.60              4.23        375.94                74.76         0.676          pass              0.261             37.8                           0.624               -1.17             -0.591                                 ok           False                  False
  MCHP           92.00               25            1.50              0.96         90.79                74.43         0.643          pass              0.612             42.7                           0.519               -6.07             -0.982            downtrend_blocked_slope           False                  False
  MPWR           81.82               22            2.44             23.62       1372.24                91.02         0.642          pass              0.299             35.6                           0.468              -10.02             -1.404            downtrend_blocked_slope           False                  False
  QCOM           86.21               29            0.67              0.86        184.42                83.64         0.637          pass              0.570             71.3                           0.528              -14.25             -1.993 downtrend_blocked_slope_and_streak           False                  False
  NXPI           91.43               35            0.02              0.05        281.01                65.46         0.635          pass              0.833             99.4                           0.792               -6.92             -1.118            downtrend_blocked_slope           False                  False
   ADI           89.29               28            1.05              2.93        395.91                64.06         0.614          pass              0.597             56.0                           0.517               -5.53             -0.928            downtrend_blocked_slope           False                  False
   HON           77.27               22            0.86              1.34        223.32                42.01         0.520          pass              0.257             41.8                           0.423               -3.27             -0.173                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-01T15:10:11.143271-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:05:07.919397-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:00:09.367331-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:55:05.861766-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:50:09.429141-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped                    {"early_entry_score": 0.2, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 720.0, "option_spread_pct": 17.39, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "AEP", "timing_score": 0.543}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped                           {"early_entry_score": 0.643, "option_liquidity_status": "wide_spread", "option_open_interest": 1263.0, "option_spread_pct": 16.22, "option_volume": 24.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.571}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.275, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 12.0, "option_spread_pct": 31.25, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.587}
2026-07-01T14:50:09.429141-04:00       entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-01", "training_samples": 5334, "window": 5}
2026-07-01T11:59:52.238657-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701151510)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701151510)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701151510)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701151510)

</details>
