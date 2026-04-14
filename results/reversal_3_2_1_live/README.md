# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 14:55:06 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$1,069.00`
- Equity: `$13,259.32`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$114.32`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback                REGN       2026-04-13                   1      8      5916.0                 6030.32        739.5         753.79      739.50        753.79          114.32                   1.93         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
  FANG     option         option FANG260515C00185000       2026-04-14                   0      7      6160.0                 6160.00          8.8           8.80      186.41        186.46            0.00                   0.00         100.0               20              1.42         38.05           38.07                  30.53                 326.0           18.0               0.07                           ok
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               22            1.34              1.78        188.34                30.53            True
  INTC           96.00               25            2.96              1.35         64.62                75.15            True
  FTNT           95.24               42            0.74              0.41         78.56                38.32            True
   XEL           94.12               17            0.73              0.41         80.27                20.44            True
  FAST           92.86               14            2.05              0.66         45.52                37.61            True
  MPWR           91.43               35            0.60              5.79       1369.75                58.48            True
  COST           90.62               32            0.59              4.03        979.12                19.04            True
  ORLY           90.48               42            0.63              0.41         93.83                24.40            True
  DXCM           88.37               43            0.67              0.29         62.99                33.61            True
  DDOG           86.11               36            0.93              0.71        109.77                53.71            True
  ADSK           85.00               40            0.56              0.89        226.76                39.97            True
  CTSH           83.78               37            0.66              0.28         60.41                30.13            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                detail
2026-04-14T14:55:06.427880-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:50:06.429660-04:00  entry_1500        entry {"allocated_cash": 6160.0, "asset_type": "option", "contract_symbol": "FANG260515C00185000", "contracts": 7, "entry_option_price": 8.8, "execution_mode": "option", "matched_signals": 20, "option_liquidity_status": "ok", "option_open_interest": 326.0, "option_spread_pct": 6.82, "option_volume": 18.0, "success_rate": 100.0, "ticker": "FANG"}
2026-04-14T14:40:05.427005-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:35:00.709827-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:30:06.440257-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:25:06.437445-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:10:06.428517-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:05:06.440824-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:00:05.431636-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T13:55:04.952325-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414145506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414145506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414145506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414145506)

</details>
