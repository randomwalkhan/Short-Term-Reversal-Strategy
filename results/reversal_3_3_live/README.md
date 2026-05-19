# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 11:55:04 EDT`
Last processed slot: `manage_1200`

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
- Equity: `$27,140.00`
- Realized PnL: `$17,837.50`
- Unrealized PnL: `$-697.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13050.0        15.28           14.5      245.93        241.32          bid_ask_mid                       14.5                bid_ask_mid                    True          -697.5                  -5.07         91.67               36              0.66         58.04            65.2                  42.55                2852.0           34.0                0.1                      ok
```

## Today's Closed Trades (2026-05-19)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TTWO     option         option TTWO260618C00250000     10          2026-05-18         2026-05-19        13.55      12.195 -1355.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           96.00               25            1.49              5.20        496.20                41.65         0.548          pass              0.571              5.2                           0.169               -2.29             -0.199                                 ok            True                  False
  GOOG           80.00               10            2.40              6.60        390.28                40.55         0.539          pass              0.061              2.4                           0.160               -0.15             -0.010                                 ok            True                  False
  ASML           82.14               28            1.35             13.94       1466.42                50.95         0.523          pass              0.337             35.9                           0.428                0.66             -0.171                                 ok            True                  False
  NVDA           87.50               32            0.83              1.29        221.77                44.74         0.513          pass              0.573             58.3                           0.550               12.20              1.133                                 ok            True                  False
  AVGO           88.89               18            2.31              6.81        417.79                42.85         0.506          pass              0.444             34.4                           0.648               -3.83             -0.120                                 ok            True                  False
  TTWO          100.00               20            1.67              2.82        240.95                33.10         0.502          pass              0.582             21.8                           0.227                6.73              1.029                                 ok            True                  False
  INTC          100.00               26            1.69              1.28        107.62               114.00         0.708          pass              0.782             68.3                           0.772               -1.67             -0.460 downtrend_blocked_slope_and_streak           False                  False
  QCOM          100.00                4            4.16              5.93        201.10                99.05         0.648          pass              0.564             32.9                           0.650                4.62              0.131                                 ok           False                  False
 CMCSA           89.47               38            0.12              0.02         24.92                60.09         0.629          pass              0.712             70.0                           0.310               -5.90             -0.668 downtrend_blocked_slope_and_streak           False                  False
  CSCO          100.00                3            2.89              2.41        117.85                49.96         0.627          pass              0.510             15.9                           0.368               22.42              2.899                                 ok           False                  False
  FTNT          100.00               43            0.43              0.39        126.33                70.72         0.605          pass              0.900             79.9                           0.546               40.07              3.260                                 ok           False                  False
  SHOP           81.08               37            1.18              0.85        102.03                78.89         0.587          pass              0.281              4.5                           0.150               -5.99             -0.976 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-19T11:55:04.964087-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:50:03.963905-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:45:02.013628-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:40:06.318992-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:35:01.898801-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:30:01.060546-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:25:05.065733-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:20:06.455937-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:15:01.967392-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-19T11:10:06.161691-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519115504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519115504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519115504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519115504)

</details>
