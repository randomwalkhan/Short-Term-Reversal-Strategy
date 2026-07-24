# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 09:40:02 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$16,265.50`
- Equity: `$31,865.50`
- Realized PnL: `$20,858.00`
- Unrealized PnL: `$1,007.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00320000       2026-07-23                   1     13     14592.5                 15600.0        11.22           12.0      320.41        325.76     last_price_stale                        NaN                unavailable                   False          1007.5                    6.9          90.0               10              1.68         30.72             0.0                  37.45               25201.0         5101.0               0.02                      ok
```

## Today's Closed Trades (2026-07-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           86.36               22            2.43             15.50        906.72               102.76         0.676          pass              0.475             52.5                           0.430               -2.10              0.412                                 ok            True                  False
   WDC           90.00               20            3.62             14.15        552.24               114.14         0.655          pass              0.495             32.0                           0.340               -7.64             -0.218                                 ok            True                  False
  ASML           93.94               33            0.96             12.15       1797.79                56.08         0.581          pass              0.705             40.5                           0.310               -0.65              0.131                                 ok            True                  False
  MPWR           81.25               32            1.90             18.56       1389.20                64.71         0.515          pass              0.316             28.2                           0.196                1.32              0.446                                 ok            True                  False
  KLAC           88.57               35            0.80              1.22        218.21                98.03         0.726          pass              0.660             64.0                           0.527               -6.28             -0.652 downtrend_blocked_slope_and_streak           False                  False
  AMAT           92.86               28            1.19              4.70        560.78                96.41         0.686          pass              0.667             45.3                           0.367               -7.70             -0.749 downtrend_blocked_slope_and_streak           False                  False
  LRCX           85.19               27            1.16              2.59        318.67                88.87         0.682          pass              0.517             65.7                           0.580               -9.78             -0.916 downtrend_blocked_slope_and_streak           False                  False
  SOXL           83.33               24            6.30              6.94        154.42               181.17         0.630          pass              0.245              0.0                           0.230              -23.29             -1.751            downtrend_blocked_slope           False                  False
  PYPL           90.00               40            0.14              0.06         55.98                61.86         0.621          pass              0.813             94.7                           0.604               20.73              1.888                                 ok           False                  False
   APP           82.22               45            0.71              1.98        398.01                79.31         0.580          pass              0.477             53.4                           0.273              -21.88             -1.854            downtrend_blocked_slope           False                  False
  META           86.36               44            0.25              1.05        605.65                54.86         0.548          pass              0.665             80.1                           0.578               -9.65             -1.026 downtrend_blocked_slope_and_streak           False                  False
  MSTR           73.68               38            1.51              0.99         93.21                85.75         0.540          pass              0.241              0.0                           0.217               -2.56              0.127                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-24T00:00:02.342132-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-07-23T15:10:05.971667-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T15:05:04.134167-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T15:00:04.002554-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T14:55:02.141413-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T14:50:05.030619-04:00       entry_1500              entry {"allocated_cash": 14592.5, "asset_type": "option", "contract_symbol": "AAPL260821C00320000", "contracts": 13, "early_entry_score": 0.378, "entry_mode": "regular", "entry_option_price": 11.225, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 25201.0, "option_spread_pct": 2.23, "option_volume": 5101.0, "success_rate": 90.0, "ticker": "AAPL", "timing_score": 0.624}
2026-07-23T14:50:05.030619-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-23", "training_samples": 5516, "window": 5}
2026-07-23T12:00:02.078304-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:55:05.041109-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:50:02.063008-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724094002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724094002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724094002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724094002)

</details>
