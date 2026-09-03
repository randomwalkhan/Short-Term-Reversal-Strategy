# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 15:50:05 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$37,600.60`
- Equity: `$74,478.10`
- Realized PnL: `$64,478.10`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261016C00110000       2026-09-03                   0     99     36877.5                 36877.5         3.72           3.72      108.86        108.56          bid_ask_mid                       3.72                bid_ask_mid                    True             0.0                    0.0         89.19               37              0.54         28.76           29.37                  36.36                2875.0          348.0               0.04                      ok
```

## Today's Closed Trades (2026-09-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CPRT     option         option CPRT261016C00032500    144          2026-09-01         2026-09-03        1.650       2.800 16560.0   69.696970 take_profit_day2_hit_at_scan
  MSTR     option         option MSTR261009C00122000     20          2026-09-02         2026-09-03       11.475      16.575 10200.0   44.444444 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI          100.00               31            0.77             10.75       2001.97                49.44         0.550          pass              0.644             16.4                           0.227                3.60              0.289                                 ok            True                  False
  REGN          100.00               20            1.09              6.50        849.25                27.66         0.533          pass              0.627             35.6                           0.368                1.95              0.050                                 ok            True                  False
  SBUX           95.24               21            0.71              0.53        106.49                21.58         0.527          pass              0.674             49.3                           0.323                1.89              0.042                                 ok            True                  False
  CSCO           87.88               33            0.79              0.60        109.20                36.36         0.519          pass              0.576             53.6                           0.350               -0.91             -0.136                                 ok            True                  False
 CMCSA           92.31               26            0.69              0.13         26.75                26.14         0.511          pass              0.607             40.3                           0.357                0.78             -0.081                                 ok            True                  False
  MNST           89.29               28            0.64              0.20         44.33               424.20         1.000          pass              0.468              0.0                           0.247               -7.06             -0.954 downtrend_blocked_slope_and_streak           False                  False
  DRAM           82.86               35            0.45              0.18         56.13                63.42         0.602          pass              0.563             86.8                           0.734               -2.82             -0.173                                 ok           False                  False
    MU           86.84               38            0.05              0.37        955.92                51.19         0.539          pass              0.719             98.6                           0.766               -1.93             -0.017                                 ok           False                  False
   STX           86.21               29            1.85             10.47        804.05                70.48         0.539          pass              0.546             66.7                           0.730               -6.66             -0.424 downtrend_blocked_slope_and_streak           False                  False
  SNPS           91.49               47            0.42              1.24        415.44                57.94         0.523          pass              0.672             37.9                           0.379                4.09              0.683                                 ok           False                  False
  PANW           87.50               48            0.08              0.19        328.40                70.92         0.517          pass              0.740             96.1                           0.497               -6.11             -0.217                                 ok           False                  False
   WDC           79.31               29            1.71              5.38        446.59                80.52         0.511          pass              0.395             72.5                           0.719               -5.94             -0.289 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-09-03T15:10:05.000086-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T15:05:01.989817-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T14:55:01.997283-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T14:50:04.996854-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 36877.5, "asset_type": "option", "contract_symbol": "CSCO261016C00110000", "contracts": 99, "early_entry_score": 0.681, "entry_mode": "regular", "entry_option_price": 3.725, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2875.0, "option_spread_pct": 4.03, "option_volume": 348.0, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.511}
2026-09-03T14:50:04.996854-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"early_entry_score": 0.577, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 18.28, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "REGN", "timing_score": 0.533}
2026-09-03T14:50:04.996854-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"early_entry_score": 0.72, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 85.0, "option_spread_pct": 12.16, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.542}
2026-09-03T14:50:04.996854-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-03", "training_samples": 5764, "window": 5}
2026-09-03T12:00:04.745572-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.52, "early_entry_score": 0.852, "early_reclaim_pct": 70.1, "entry_ask": 9.55, "entry_bid": 9.3, "entry_mode": "early", "entry_option_price": 9.425, "hypothetical_budget": 37239.05, "hypothetical_contracts": 39, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 365.0, "option_spread_pct": 2.65, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.412, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.852, "early_reclaim_pct": 70.1, "matched_signals": 41, "recovery_stability_score": 0.58, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T11:55:01.936733-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:50:04.853534-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903155005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903155005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903155005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903155005)

</details>
