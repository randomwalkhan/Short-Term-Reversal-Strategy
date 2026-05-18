# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 11:45:01 EDT`
Last processed slot: `early_entry_1145`

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
- Equity: `$29,142.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-50.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13500.0        13.55           13.5      241.03         240.5          bid_ask_mid                       13.5                bid_ask_mid                    True           -50.0                  -0.37         97.62               42              0.58         61.06           61.93                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-15         2026-05-18        29.05      26.145 -1452.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               28            1.51              1.15        108.28               115.99         0.694          pass              0.762             57.6                           0.313               11.85              0.736                                 ok            True                  False
  QCOM           89.47               19            1.90              2.67        200.34                99.06         0.665          pass              0.534             51.7                           0.635               17.40              1.169                                 ok            True                  False
  CSCO           90.00               20            1.24              1.03        117.77                49.84         0.614          pass              0.492             32.6                           0.374               26.03              2.712                                 ok            True                  False
  AMGN           91.67               12            1.08              2.47        325.25                26.25         0.552          pass              0.472             30.7                           0.292                0.42              0.105                                 ok            True                  False
  SNPS           94.12               17            2.32              8.16        498.92                42.05         0.530          pass              0.495              6.2                           0.179               -1.35             -0.024                                 ok            True                  False
  AAPL           85.71               14            1.51              3.17        298.87                22.88         0.528          pass              0.254              7.4                           0.147                6.91              0.687                                 ok            True                  False
  MSFT           82.61               23            1.08              3.20        420.55                29.78         0.502          pass              0.358             50.6                           0.384                0.90              0.018                                 ok            True                  False
   TXN           93.75               32            0.33              0.70        302.43                68.84         0.688          pass              0.805             74.4                           0.578                7.96              0.943                                 ok           False                  False
  SHOP           86.05               43            0.08              0.06        100.26                79.48         0.618          pass              0.709             95.5                           0.556              -21.44             -1.949 downtrend_blocked_slope_and_streak           False                  False
  INSM           42.86               14            3.59              2.74        107.96               111.34         0.587          pass              0.132             15.5                           0.177              -24.85             -2.319 downtrend_blocked_slope_and_streak           False                  False
  SBUX           96.97               33            0.23              0.17        106.74                32.79         0.523          pass              0.867             87.1                           0.467                2.12              0.224                                 ok           False                  False
  META           73.08               26            1.08              4.66        612.23                37.75         0.515          pass              0.328             56.7                           0.508               -0.47              0.048                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-18T11:45:01.537610-04:00 early_entry_1145 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:40:04.531844-04:00 early_entry_1140 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:35:01.580218-04:00 early_entry_1135 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:30:01.530896-04:00 early_entry_1130 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00 early_entry_1125 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00      manage_1130          exit                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "CDNS260618C00330000", "fill_price": 26.145, "pnl": -1452.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CDNS"}
2026-05-18T11:20:01.549476-04:00 early_entry_1120 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:15:03.521300-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:10:02.609364-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:05:05.558676-04:00 early_entry_1105         entry {"allocated_cash": 13550.0, "asset_type": "option", "contract_symbol": "TTWO260618C00250000", "contracts": 10, "early_entry_score": 0.906, "entry_mode": "early", "entry_option_price": 13.55, "execution_mode": "option", "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 3069.0, "option_spread_pct": 11.07, "option_volume": 22.0, "success_rate": 97.62, "ticker": "TTWO", "timing_score": 0.402}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518114501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518114501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518114501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518114501)

</details>
