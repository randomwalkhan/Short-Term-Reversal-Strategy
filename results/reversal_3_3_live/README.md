# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 10:00:04 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$17,608.25`
- Equity: `$35,233.25`
- Realized PnL: `$24,370.75`
- Unrealized PnL: `$862.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260918C00100000       2026-08-06                   1     15     16762.5                 17625.0        11.18          11.75      100.37         99.47          bid_ask_mid                      11.75                bid_ask_mid                    True           862.5                   5.15          85.0               40              0.68         79.69           87.83                  86.71               28020.0         1406.0               0.03                      ok
```

## Today's Closed Trades (2026-08-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TMUS           92.86               28            0.92              1.16        179.47                57.01         0.627          pass              0.673             49.1                           0.512               -0.99             -0.150                                 ok            True                  False
    MU           80.65               31            2.04             12.56        876.09               110.38         0.623          pass              0.228              2.8                           0.040               -6.24              0.158                                 ok            True                  False
  INSM           71.43               21            2.12              1.96        131.71               110.04         0.750          pass              0.162              4.6                           0.125               21.35              1.493                                 ok           False                  False
  ALNY           87.80               41            0.48              0.73        215.81               128.30         0.622          pass              0.715             81.5                           0.774              -20.86             -3.042            downtrend_blocked_slope           False                  False
  INTC           84.62               39            0.37              0.26         99.70                86.24         0.617          pass              0.528             50.0                           0.342                7.72              1.456                                 ok           False                  False
  DRAM           77.78               27            3.25              1.17         50.94               108.98         0.592          pass              0.180              2.3                           0.047               -6.45              0.295                                 ok           False                  False
  CTAS           89.74               39            0.12              0.18        202.07                37.18         0.548          pass              0.775             88.9                           0.759               -1.95             -0.546 downtrend_blocked_slope_and_streak           False                  False
   CSX           92.31               26            0.64              0.23         50.60                29.04         0.540          pass              0.636             49.0                           0.532               -5.37             -0.310 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           90.62               32            0.13              0.06         62.73                30.17         0.536          pass              0.755             90.5                           0.736                3.55              0.184                                 ok           False                  False
   ADP           96.55               29            0.48              0.92        273.12                34.67         0.525          pass              0.830             83.7                           0.561                8.84              0.702                                 ok           False                  False
   PEP           82.14               28            0.31              0.30        138.31                22.07         0.523          pass              0.440             70.3                           0.744                1.00             -0.129                                 ok           False                  False
  AAPL           93.02               43            0.21              0.45        312.22                37.99         0.514          pass              0.791             64.1                           0.391               -6.38             -1.066 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-07T10:00:04.307079-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "matched_signals": 36, "recovery_stability_score": 0.651, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T00:00:06.807009-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 93}
2026-08-06T15:10:06.321105-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T15:05:05.205099-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T15:00:02.209761-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T14:55:01.108594-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T14:50:04.202564-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"allocated_cash": 16762.5, "asset_type": "option", "contract_symbol": "INTC260918C00100000", "contracts": 15, "early_entry_score": 0.652, "entry_mode": "regular", "entry_option_price": 11.175, "execution_mode": "option", "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 28020.0, "option_spread_pct": 3.13, "option_volume": 1406.0, "success_rate": 85.0, "ticker": "INTC", "timing_score": 0.565}
2026-08-06T14:50:04.202564-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-06", "training_samples": 5584, "window": 5}
2026-08-06T12:00:02.173564-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:55:01.207054-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807100004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807100004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807100004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807100004)

</details>
