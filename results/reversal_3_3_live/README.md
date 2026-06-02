# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 11:05:01 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$35,244.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$1,575.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AMZN     option         option AMZN260717C00260000       2026-06-02                   0     15     16200.0                 17775.0         10.8          11.85      259.57        260.31          bid_ask_mid                      11.85                bid_ask_mid                    True          1575.0                   9.72         90.62               32              0.65         30.52           31.95                  24.44                8913.0          913.0               0.02                      ok
```

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           84.85               33            0.80              5.78       1032.26               101.73         0.728          pass              0.528             57.6                           0.292               50.61              4.605                                 ok            True                  False
  FTNT          100.00               12            2.02              2.08        146.25                71.69         0.688          pass              0.641             53.1                           0.590               13.97              1.235                                 ok            True                  False
  MNST           95.00               20            1.33              0.83         88.74                49.60         0.625          pass              0.639             36.6                           0.444               -0.71              0.179                                 ok            True                  False
  MELI           88.89               18            2.13             25.85       1719.90                60.28         0.615          pass              0.435             27.5                           0.367                6.82              0.706                                 ok            True                  False
  INTC           96.55               29            1.12              0.85        108.96                88.85         0.582          pass              0.814             76.4                           0.858               -0.06             -0.100                                 ok            True                  False
  AMGN           90.00               20            0.79              1.83        328.35                20.27         0.520          pass              0.571             61.8                           0.729                0.66              0.041                                 ok            True                  False
  CDNS           90.48               21            1.88              5.46        411.82                44.19         0.502          pass              0.525             40.5                           0.518               17.45              1.727                                 ok            True                  False
  INSM           50.00               12            3.87              2.87        104.80               110.78         0.679          pass              0.156             25.0                           0.596               -4.87             -0.317            downtrend_blocked_slope           False                  False
   WMT           84.21               19            1.05              0.84        114.24                32.65         0.563          pass              0.320             30.6                           0.368              -14.95             -1.695 downtrend_blocked_slope_and_streak           False                  False
   HON           77.78                9            1.48              2.44        235.49                24.20         0.542          pass              0.117             21.0                           0.300                7.28              0.964                                 ok           False                  False
  REGN           89.19               37            0.35              1.48        600.03                42.53         0.537          pass              0.709             76.9                           0.755               -4.80             -0.621 downtrend_blocked_slope_and_streak           False                  False
    ZS          100.00                1            9.59             10.45        151.23               157.27         0.531          pass              0.454              0.5                           0.171              -19.41             -2.847            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-02T11:05:01.381854-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:00:04.363054-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:55:06.617729-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:50:06.041869-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:45:01.434257-04:00 early_entry_1045         entry {"allocated_cash": 16200.0, "asset_type": "option", "contract_symbol": "AMZN260717C00260000", "contracts": 15, "early_entry_score": 0.702, "entry_mode": "early", "entry_option_price": 10.8, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 8913.0, "option_spread_pct": 1.85, "option_volume": 913.0, "success_rate": 90.62, "ticker": "AMZN", "timing_score": 0.457}
2026-06-02T10:40:04.457109-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:35:04.553797-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:30:04.405006-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:25:01.235572-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:20:01.327977-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602110501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602110501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602110501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602110501)

</details>
