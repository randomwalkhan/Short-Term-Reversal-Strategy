# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 10:35:03 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$29,755.00`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$562.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 14310.0        15.28          15.90      245.93        247.20          bid_ask_mid                      15.90                bid_ask_mid                    True           562.5                   4.09         91.67               36              0.66         58.04           59.36                  42.55                2852.0           34.0               0.10                      ok
  TTWO     option         option TTWO260618C00250000       2026-05-18                   1     10     13550.0                 13550.0        13.55          13.55      241.03        238.75          bid_ask_mid                      13.55                bid_ask_mid                    True             0.0                   0.00         97.62               42              0.58         61.06           65.42                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           81.25               32            0.76              1.55        291.02                90.65         0.723          pass              0.445             64.2                           0.479               -0.99             -0.204                                 ok            True                  False
   TXN           86.67               15            1.57              3.30        299.19                69.24         0.687          pass              0.446             55.4                           0.589                5.30              0.685                                 ok            True                  False
  FTNT          100.00               42            0.60              0.53        126.27                70.72         0.601          pass              0.877             72.4                           0.581               39.84              3.252                                 ok            True                   True
 GOOGL           81.25               16            1.61              4.47        395.03                40.53         0.556          pass              0.221             30.7                           0.318                0.55              0.040                                 ok            True                  False
  GOOG           84.21               19            1.48              4.07        391.36                40.55         0.544          pass              0.334             35.8                           0.343                0.79              0.032                                 ok            True                  False
  SNPS           96.88               32            0.97              3.37        496.99                41.65         0.540          pass              0.680             26.4                           0.164               -1.77             -0.175                                 ok            True                  False
  NVDA           85.00               20            1.81              2.82        221.11                44.74         0.526          pass              0.278              8.5                           0.152               11.09              1.087                                 ok            True                  False
  ASML           82.14               28            1.61             16.59       1465.28                50.95         0.507          pass              0.292             21.5                           0.225                0.40             -0.182                                 ok            True                  False
  INTC          100.00               10            4.68              3.54        106.65               114.00         0.631          pass              0.500             12.3                           0.150               -4.66             -0.600 downtrend_blocked_slope_and_streak           False                  False
  MNST           75.00               16            1.57              0.97         88.12                49.83         0.616          pass              0.175             24.5                           0.555               14.97              1.490                                 ok           False                  False
  CSCO          100.00                3            3.23              2.69        117.73                49.96         0.607          pass              0.479              6.1                           0.091               21.99              2.883                                 ok           False                  False
  QCOM          100.00                1            5.41              7.71        200.33                99.05         0.591          pass              0.497             12.7                           0.243                3.25              0.071                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-19T10:35:03.933477-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:30:01.041969-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:25:01.081339-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:20:03.970688-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:15:01.057449-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:10:01.046495-04:00 early_entry_1010         entry {"allocated_cash": 13747.5, "asset_type": "option", "contract_symbol": "PANW260618C00250000", "contracts": 9, "early_entry_score": 0.729, "entry_mode": "early", "entry_option_price": 15.275, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2852.0, "option_spread_pct": 10.15, "option_volume": 34.0, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.462}
2026-05-19T10:05:01.031829-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-19T10:00:03.926915-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-19T00:00:06.432342-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92}
2026-05-18T15:10:01.689138-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519103503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519103503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519103503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519103503)

</details>
