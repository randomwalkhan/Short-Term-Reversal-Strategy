# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 10:20:03 EDT`
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
- Equity: `$27,942.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-1,250.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13297.5        15.28          14.78      245.93        245.15          bid_ask_mid                      14.78                bid_ask_mid                    True          -450.0                  -3.27         91.67               36              0.66         58.04           60.21                  42.55                2852.0           34.0               0.10                      ok
  TTWO     option         option TTWO260618C00250000       2026-05-18                   1     10     13550.0                 12750.0        13.55          12.75      241.03        239.76          bid_ask_mid                      12.75                bid_ask_mid                    True          -800.0                  -5.90         97.62               42              0.58         61.06           61.38                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.91               11            2.24              4.70        298.58                69.24         0.679          pass              0.474             36.3                           0.287                4.58              0.654                                 ok            True                  False
  FTNT          100.00               41            0.62              0.55        126.27                70.72         0.607          pass              0.875             71.5                           0.595               39.81              3.252                                 ok            True                   True
 GOOGL           80.00               15            1.70              4.71        394.92                40.53         0.555          pass              0.169             26.9                           0.393                0.46              0.036                                 ok            True                  False
  GOOG           83.33               18            1.63              4.49        391.18                40.55         0.540          pass              0.284             29.1                           0.401                0.63              0.025                                 ok            True                  False
  SNPS           97.06               34            0.89              3.10        497.10                41.65         0.531          pass              0.710             32.3                           0.222               -1.69             -0.171                                 ok            True                  False
  NVDA           85.71               21            1.69              2.62        221.20                44.74         0.529          pass              0.323             15.0                           0.190               11.23              1.093                                 ok            True                  False
   CSX           87.88               33            0.56              0.18         46.12                31.65         0.513          pass              0.556             46.9                           0.601                2.02              0.248                                 ok            True                  False
  ASML           82.14               28            1.68             17.30       1464.98                50.95         0.505          pass              0.257              9.8                           0.097                0.33             -0.186                                 ok            True                  False
  NXPI           75.00               24            1.39              2.83        290.47                90.65         0.726          pass              0.270             34.6                           0.229               -1.61             -0.233                                 ok           False                  False
  INTC          100.00                9            4.87              3.69        106.59               114.00         0.628          pass              0.476              4.4                           0.193               -4.85             -0.609 downtrend_blocked_slope_and_streak           False                  False
  MNST           66.67               12            1.83              1.13         88.05                49.83         0.614          pass              0.111             12.0                           0.201               14.67              1.478                                 ok           False                  False
  CSCO          100.00                3            3.42              2.84        117.66                49.96         0.597          pass              0.460              0.0                           0.183               21.76              2.875                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-19T10:20:03.970688-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:15:01.057449-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:10:01.046495-04:00 early_entry_1010         entry {"allocated_cash": 13747.5, "asset_type": "option", "contract_symbol": "PANW260618C00250000", "contracts": 9, "early_entry_score": 0.729, "entry_mode": "early", "entry_option_price": 15.275, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2852.0, "option_spread_pct": 10.15, "option_volume": 34.0, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.462}
2026-05-19T10:05:01.031829-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-19T10:00:03.926915-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-19T00:00:06.432342-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92}
2026-05-18T15:10:01.689138-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T15:05:01.585453-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T15:00:05.590805-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T14:55:05.590920-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519102003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519102003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519102003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519102003)

</details>
