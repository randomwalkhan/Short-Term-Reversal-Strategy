# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 11:15:04 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$17,469.25`
- Equity: `$35,694.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$2,025.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AMZN     option         option AMZN260717C00260000       2026-06-02                   0     15     16200.0                 18225.0         10.8          12.15      259.57        260.48          bid_ask_mid                      12.15                bid_ask_mid                    True          2025.0                   12.5         90.62               32              0.65         30.52           32.18                  24.44                8913.0          913.0               0.02                      ok
```

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           94.12               17            1.48              0.92         88.70                49.60         0.634          pass              0.575             29.4                           0.496               -0.86              0.172                                 ok            True                  False
  MELI           87.50               16            2.26             27.42       1719.23                60.28         0.619          pass              0.371             23.2                           0.278                6.68              0.700                                 ok            True                  False
  INTC           96.97               33            0.86              0.66        109.05                88.85         0.573          pass              0.856             81.8                           0.730                0.20             -0.088                                 ok            True                   True
  CDNS          100.00               11            2.44              7.08        411.12                44.19         0.547          pass              0.530             22.9                           0.263               16.78              1.701                                 ok            True                  False
  FTNT          100.00                9            2.28              2.35        146.13                71.69         0.691          pass              0.610             47.0                           0.474               13.67              1.223                                 ok           False                  False
  INSM           50.00               12            3.86              2.86        104.80               110.78         0.680          pass              0.157             25.2                           0.427               -4.86             -0.317            downtrend_blocked_slope           False                  False
   WMT           78.57               14            1.28              1.03        114.16                32.65         0.575          pass              0.129             15.0                           0.325              -15.16             -1.706 downtrend_blocked_slope_and_streak           False                  False
  REGN           89.19               37            0.35              1.49        600.02                42.53         0.536          pass              0.709             76.7                           0.754               -4.80             -0.621 downtrend_blocked_slope_and_streak           False                  False
   HON           71.43                7            1.81              3.00        235.25                24.20         0.526          pass              0.064              3.9                           0.270                6.91              0.948                                 ok           False                  False
    ZS          100.00                1            9.72             10.60        151.17               157.27         0.516          pass              0.462              3.6                           0.131              -19.53             -2.854            downtrend_blocked_slope           False                  False
   ADP          100.00                7            2.75              4.49        231.81                34.26         0.511          pass              0.525             24.7                           0.593                1.96              0.282                                 ok           False                  False
 GOOGL           85.71               14            1.64              4.33        374.52                26.14         0.511          pass              0.427             65.5                           0.577               -6.74             -0.460            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-02T11:15:04.236525-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:10:04.323542-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:05:01.381854-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:00:04.363054-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:55:06.617729-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:50:06.041869-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:45:01.434257-04:00 early_entry_1045         entry {"allocated_cash": 16200.0, "asset_type": "option", "contract_symbol": "AMZN260717C00260000", "contracts": 15, "early_entry_score": 0.702, "entry_mode": "early", "entry_option_price": 10.8, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 8913.0, "option_spread_pct": 1.85, "option_volume": 913.0, "success_rate": 90.62, "ticker": "AMZN", "timing_score": 0.457}
2026-06-02T10:40:04.457109-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:35:04.553797-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:30:04.405006-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602111504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602111504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602111504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602111504)

</details>
