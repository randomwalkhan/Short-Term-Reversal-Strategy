# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 11:20:06 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$14,090.00`
- Equity: `$27,477.50`
- Realized PnL: `$17,837.50`
- Unrealized PnL: `$-360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13387.5        15.28          14.88      245.93        244.98          bid_ask_mid                      14.88                bid_ask_mid                    True          -360.0                  -2.62         91.67               36              0.66         58.04           59.06                  42.55                2852.0           34.0                0.1                      ok
```

## Today's Closed Trades (2026-05-19)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TTWO     option         option TTWO260618C00250000     10          2026-05-18         2026-05-19        13.55      12.195 -1355.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           92.31               26            0.80              1.69        299.88                69.24         0.673          pass              0.734             77.2                           0.763                6.12              0.720                                 ok            True                  False
  GOOG           80.00               10            2.08              5.71        390.66                40.55         0.561          pass              0.086              9.9                           0.181                0.18              0.005                                 ok            True                  False
 GOOGL           80.00               10            2.23              6.20        394.28                40.53         0.556          pass              0.067              3.9                           0.151               -0.09              0.011                                 ok            True                  False
  ASML           82.76               29            1.13             11.62       1467.41                50.95         0.532          pass              0.393             46.6                           0.555                0.89             -0.160                                 ok            True                  False
  SNPS           97.06               34            0.88              3.06        497.12                41.65         0.529          pass              0.746             44.3                           0.500               -1.68             -0.171                                 ok            True                  False
  NVDA           87.88               33            0.65              1.02        221.88                44.74         0.518          pass              0.617             67.1                           0.741               12.40              1.141                                 ok            True                  False
  INTC          100.00               23            1.96              1.48        107.53               114.00         0.711          pass              0.747             63.3                           0.820               -1.94             -0.472 downtrend_blocked_slope_and_streak           False                  False
  TEAM           88.89               36            1.59              1.00         89.01               113.67         0.664          pass              0.479              0.7                           0.216               -4.70             -0.641           downtrend_blocked_streak           False                  False
  QCOM          100.00                2            4.66              6.64        200.79                99.05         0.631          pass              0.538             24.8                           0.495                4.08              0.107                                 ok           False                  False
  CSCO          100.00                3            2.93              2.44        117.84                49.96         0.625          pass              0.507             14.9                           0.344               22.38              2.898                                 ok           False                  False
  SHOP           83.33               42            0.46              0.33        102.25                78.89         0.605          pass              0.538             62.9                           0.272               -5.31             -0.943 downtrend_blocked_slope_and_streak           False                  False
    MU           83.78               37            0.03              0.13        681.48                90.51         0.598          pass              0.639             99.4                           0.930                6.43              0.754                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                             detail
2026-05-19T11:20:06.455937-04:00 early_entry_1120 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:15:01.967392-04:00 early_entry_1115 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:10:06.161691-04:00 early_entry_1110 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:05:01.947940-04:00 early_entry_1105 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:00:04.023655-04:00 early_entry_1100 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:00:04.023655-04:00      manage_1100          exit {"asset_type": "option", "contract_symbol": "TTWO260618C00250000", "fill_price": 12.195, "pnl": -1355.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TTWO"}
2026-05-19T10:55:01.036439-04:00 early_entry_1055 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T10:50:05.059636-04:00 early_entry_1050 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T10:45:01.038335-04:00 early_entry_1045 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T10:40:01.036176-04:00 early_entry_1040 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519112006)

</details>
