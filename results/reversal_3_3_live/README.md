# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 11:30:01 EDT`
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

- Cash: `$15,642.50`
- Equity: `$29,192.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13550.0        13.55          13.55      241.03        240.59          bid_ask_mid                      13.55                bid_ask_mid                    True             0.0                    0.0         97.62               42              0.58         61.06           61.74                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-15         2026-05-18        29.05      26.145 -1452.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           92.00               25            0.86              1.81        301.95                68.84         0.696          pass              0.592             34.1                           0.267                7.40              0.919                                 ok            True                  False
  INTC          100.00               27            1.81              1.38        108.18               115.99         0.682          pass              0.728             49.0                           0.318               11.51              0.722                                 ok            True                  False
  CSCO           88.24               17            1.39              1.15        117.72                49.84         0.621          pass              0.402             24.5                           0.321               25.84              2.706                                 ok            True                  False
  AMGN           91.67               12            1.12              2.56        325.21                26.25         0.550          pass              0.464             28.2                           0.204                0.38              0.103                                 ok            True                  False
  SNPS          100.00               15            2.43              8.53        498.76                42.05         0.546          pass              0.493              1.9                           0.134               -1.46             -0.029                                 ok            True                  False
  AAPL           85.71               14            1.59              3.35        298.80                22.88         0.523          pass              0.231              0.0                           0.153                6.82              0.683                                 ok            True                  False
  MSFT           82.61               23            1.07              3.16        420.57                29.78         0.503          pass              0.360             51.3                           0.297                0.92              0.019                                 ok            True                  False
  NXPI           84.62               39            0.11              0.23        291.40                90.58         0.724          pass              0.639             83.5                           0.457                0.14             -0.041                                 ok           False                  False
  QCOM          100.00                4            3.28              4.63        199.51                99.06         0.688          pass              0.518             16.4                           0.343               15.74              1.105                                 ok           False                  False
  INSM           65.22               23            2.55              1.95        108.31               111.34         0.631          pass              0.270             40.1                           0.310              -24.03             -2.270 downtrend_blocked_slope_and_streak           False                  False
  SHOP           86.05               43            0.25              0.18        100.20                79.48         0.606          pass              0.680             85.9                           0.469              -21.58             -1.957 downtrend_blocked_slope_and_streak           False                  False
  MCHP           85.71               35            0.71              0.47         93.65                53.01         0.524          pass              0.518             48.8                           0.373               -2.22             -0.540 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-18T11:30:01.530896-04:00 early_entry_1130 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00 early_entry_1125 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00      manage_1130          exit                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "CDNS260618C00330000", "fill_price": 26.145, "pnl": -1452.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CDNS"}
2026-05-18T11:20:01.549476-04:00 early_entry_1120 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:15:03.521300-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:10:02.609364-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:05:05.558676-04:00 early_entry_1105         entry {"allocated_cash": 13550.0, "asset_type": "option", "contract_symbol": "TTWO260618C00250000", "contracts": 10, "early_entry_score": 0.906, "entry_mode": "early", "entry_option_price": 13.55, "execution_mode": "option", "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 3069.0, "option_spread_pct": 11.07, "option_volume": 22.0, "success_rate": 97.62, "ticker": "TTWO", "timing_score": 0.402}
2026-05-18T11:00:09.683441-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-18T10:27:37.648386-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-18T03:00:02.728743-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518113001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518113001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518113001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518113001)

</details>
