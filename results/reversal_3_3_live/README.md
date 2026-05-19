# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 10:10:01 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$1,895.00`
- Equity: `$28,442.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-750.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13747.5        15.28          15.28      245.93        246.40          bid_ask_mid                      15.28                bid_ask_mid                    True             0.0                   0.00         91.67               36              0.66         58.04           58.04                  42.55                2852.0           34.0               0.10                      ok
  TTWO     option         option TTWO260618C00250000       2026-05-18                   1     10     13550.0                 12800.0        13.55          12.80      241.03        239.55          bid_ask_mid                      12.80                bid_ask_mid                    True          -750.0                  -5.54         97.62               42              0.58         61.06           61.34                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           92.31               13            1.78              3.75        298.99                69.24         0.694          pass              0.565             49.2                           0.365                5.07              0.675                                 ok            True                  False
  SNPS           97.14               35            0.54              1.90        497.62                41.65         0.547          pass              0.797             58.5                           0.382               -1.35             -0.155                                 ok            True                  False
 GOOGL           84.62               26            1.08              3.00        395.66                40.53         0.527          pass              0.443             53.5                           0.622                1.09              0.064                                 ok            True                  False
  NVDA           88.00               25            1.41              2.19        221.38                44.74         0.526          pass              0.418             17.2                           0.287               11.55              1.106                                 ok            True                  False
  ASML           82.14               28            1.41             14.51       1466.17                50.95         0.523          pass              0.302             24.3                           0.183                0.61             -0.173                                 ok            True                  False
  GOOG           85.71               28            1.01              2.77        391.92                40.55         0.516          pass              0.493             56.3                           0.631                1.27              0.054                                 ok            True                  False
  AVGO           90.91               11            3.05              8.97        416.86                42.85         0.514          pass              0.360              3.8                           0.113               -4.56             -0.154                                 ok            True                  False
   CSX           87.88               33            0.57              0.19         46.12                31.65         0.512          pass              0.552             45.9                           0.587                2.01              0.247                                 ok            True                  False
  FAST           91.30               23            1.01              0.31         43.87                22.17         0.506          pass              0.576             45.7                           0.602               -1.75             -0.205                                 ok            True                  False
    MU           81.48               27            2.67             12.75        676.07                90.51         0.502          pass              0.237             11.3                           0.133                3.61              0.632                                 ok            True                  False
  NXPI           77.78               27            1.17              2.39        290.66                90.65         0.725          pass              0.320             44.8                           0.330               -1.40             -0.223                                 ok           False                  False
  INSM           75.61               41            0.64              0.48        106.94               111.34         0.718          pass              0.475             67.8                           0.526              -23.65             -1.662 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-19T10:10:01.046495-04:00 early_entry_1010          entry {"allocated_cash": 13747.5, "asset_type": "option", "contract_symbol": "PANW260618C00250000", "contracts": 9, "early_entry_score": 0.729, "entry_mode": "early", "entry_option_price": 15.275, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2852.0, "option_spread_pct": 10.15, "option_volume": 34.0, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.462}
2026-05-19T10:05:01.031829-04:00 early_entry_1005  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-19T10:00:03.926915-04:00 early_entry_1000  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-19T00:00:06.432342-04:00     data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92}
2026-05-18T15:10:01.689138-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T15:05:01.585453-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T15:00:05.590805-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T14:55:05.590920-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T14:50:01.599355-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-18", "training_samples": 5028, "window": 5}
2026-05-18T14:50:01.599355-04:00       entry_1500  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519101001)

</details>
