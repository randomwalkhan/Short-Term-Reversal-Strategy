# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 15:25:02 EDT`
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

- Cash: `$15,119.25`
- Equity: `$29,364.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$140.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260821C00290000       2026-07-17                   0      7     14105.0                 14245.0        20.15          20.35      284.95        283.04          bid_ask_mid                      20.35                bid_ask_mid                    True           140.0                   0.99          90.0               20              2.15         62.88           65.54                  64.46                 207.0          231.0               0.09                      ok
```

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               14            0.72              0.31         61.29                33.43         0.613          pass              0.616             42.6                           0.522                0.11              0.075                      ok            True                  False
   KHC           90.91               11            1.24              0.23         26.13                36.78         0.589          pass              0.419             20.7                           0.322                2.11              0.344                      ok            True                  False
   TXN           88.24               17            2.81              5.73        288.77                64.46         0.576          pass              0.419             31.7                           0.264               -3.43             -0.241                      ok            True                  False
   ADI           86.96               23            1.82              4.86        378.45                54.65         0.572          pass              0.478             49.5                           0.330               -0.95             -0.021                      ok            True                  False
  ASML           91.67               24            2.23             27.87       1772.92                64.12         0.547          pass              0.613             51.1                           0.303               -1.37             -0.073                      ok            True                  False
  NXPI           86.96               23            1.90              3.61        269.11                54.99         0.532          pass              0.498             57.6                           0.447               -2.87             -0.243                      ok            True                  False
  GILD           89.47               19            1.25              1.19        135.79                34.67         0.525          pass              0.401             11.9                           0.256                2.54              0.099                      ok            True                  False
   CSX           90.00               20            0.82              0.29         50.77                21.08         0.513          pass              0.480             32.0                           0.364                3.24              0.399                      ok            True                  False
  AVGO           82.14               28            1.16              3.05        373.14                50.81         0.512          pass              0.450             73.8                           0.501                2.67              0.255                      ok            True                  False
   ADP           96.67               30            0.58              1.04        256.11                34.79         0.510          pass              0.797             70.8                           0.646                5.28              0.579                      ok            True                   True
  BKNG           85.71               21            1.75              2.26        183.64                41.98         0.506          pass              0.411             44.9                           0.567               -1.72              0.012                      ok            True                  False
  KLAC           81.25               16            3.71              5.70        216.93               106.93         0.633          pass              0.271             44.9                           0.308              -10.32             -0.575 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-17T15:10:06.696610-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T15:05:06.030959-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T15:00:09.838561-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T14:55:11.420522-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T14:50:08.434742-04:00       entry_1500                   entry {"allocated_cash": 14105.0, "asset_type": "option", "contract_symbol": "TXN260821C00290000", "contracts": 7, "early_entry_score": 0.537, "entry_mode": "regular", "entry_option_price": 20.15, "execution_mode": "option", "matched_signals": 20, "option_liquidity_status": "ok", "option_open_interest": 207.0, "option_spread_pct": 8.93, "option_volume": 231.0, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.602}
2026-07-17T14:50:08.434742-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                         {"early_entry_score": 0.572, "option_liquidity_status": "low_volume", "option_open_interest": 709.0, "option_spread_pct": 11.11, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.602}
2026-07-17T14:50:08.434742-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-17", "training_samples": 5456, "window": 5}
2026-07-17T12:00:05.871771-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:55:01.882856-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:50:01.906755-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717152502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717152502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717152502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717152502)

</details>
