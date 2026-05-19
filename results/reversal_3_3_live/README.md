# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 11:30:01 EDT`
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
- Equity: `$27,207.50`
- Realized PnL: `$17,837.50`
- Unrealized PnL: `$-630.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13117.5        15.28          14.58      245.93        244.51          bid_ask_mid                      14.58                bid_ask_mid                    True          -630.0                  -4.58         91.67               36              0.66         58.04            59.0                  42.55                2852.0           34.0                0.1                      ok
```

## Today's Closed Trades (2026-05-19)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TTWO     option         option TTWO260618C00250000     10          2026-05-18         2026-05-19        13.55      12.195 -1355.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           93.55               31            0.54              1.13        300.12                69.24         0.661          pass              0.822             84.7                           0.816                6.40              0.732                                 ok            True                   True
  SNPS           96.43               28            1.28              4.45        496.52                41.65         0.543          pass              0.631             18.9                           0.313               -2.08             -0.189                                 ok            True                  False
  GOOG           80.00               10            2.34              6.43        390.35                40.55         0.543          pass              0.069              4.9                           0.195               -0.09             -0.008                                 ok            True                  False
 GOOGL           80.00               10            2.47              6.86        394.00                40.53         0.537          pass              0.069              4.9                           0.179               -0.33             -0.000                                 ok            True                  False
  NVDA           87.50               32            0.83              1.30        221.76                44.74         0.512          pass              0.572             57.9                           0.584               12.20              1.133                                 ok            True                  False
  ASML           82.14               28            1.57             16.23       1465.43                50.95         0.509          pass              0.304             25.4                           0.295                0.44             -0.181                                 ok            True                  False
  AVGO           85.71               14            2.73              8.04        417.26                42.85         0.502          pass              0.297             22.6                           0.353               -4.24             -0.140                                 ok            True                  False
  INTC          100.00               19            2.40              1.82        107.39               114.00         0.709          pass              0.696             54.9                           0.625               -2.39             -0.493 downtrend_blocked_slope_and_streak           False                  False
  TEAM           87.88               33            1.96              1.23         88.91               113.67         0.655          pass              0.431              0.6                           0.205               -5.06             -0.658           downtrend_blocked_streak           False                  False
  QCOM          100.00                2            4.59              6.54        200.84                99.05         0.635          pass              0.541             26.0                           0.467                4.15              0.111                                 ok           False                  False
  CSCO          100.00                3            3.04              2.53        117.80                49.96         0.619          pass              0.497             11.7                           0.225               22.24              2.892                                 ok           False                  False
  SHOP           82.50               40            0.63              0.45        102.20                78.89         0.605          pass              0.474             49.1                           0.223               -5.47             -0.951 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                             detail
2026-05-19T11:30:01.060546-04:00 early_entry_1130 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:25:05.065733-04:00 early_entry_1125 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:20:06.455937-04:00 early_entry_1120 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:15:01.967392-04:00 early_entry_1115 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:10:06.161691-04:00 early_entry_1110 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:05:01.947940-04:00 early_entry_1105 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:00:04.023655-04:00 early_entry_1100 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:00:04.023655-04:00      manage_1100          exit {"asset_type": "option", "contract_symbol": "TTWO260618C00250000", "fill_price": 12.195, "pnl": -1355.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TTWO"}
2026-05-19T10:55:01.036439-04:00 early_entry_1055 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T10:50:05.059636-04:00 early_entry_1050 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519113001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519113001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519113001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519113001)

</details>
