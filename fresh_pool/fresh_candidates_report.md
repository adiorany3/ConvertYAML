# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=212ms, nekobox=228ms, status=yes)
2. `AKUN-002-ICOOK-VLESS-WS-64MS` (url=205ms, nekobox=234ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-70MS` (url=218ms, nekobox=229ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-97MS` (url=206ms, nekobox=231ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=217ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=220ms, nekobox=231ms, status=yes)
7. `AKUN-007-ZENFO-1-VLESS-WS-111MS` (url=212ms, nekobox=242ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-129MS` (url=229ms, nekobox=247ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS` (url=218ms, nekobox=178ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-111MS`
11. `AKUN-010-RMGYVPN-VLESS-WS-144MS`
12. `AKUN-018-UNKNOWN-VLESS-WS-247MS` (url=369ms, status=HTTP 204)
13. `AKUN-019-CLOUDFLARE-VLESS-WS-388MS` (url=663ms, status=HTTP 204)
14. `AKUN-020-CLOUDFLARE-VLESS-WS-398MS` (url=713ms, status=HTTP 204)
15. `AKUN-021-CLOUDFLARE-VLESS-WS-445MS` (url=804ms, status=HTTP 204)
16. `AKUN-026-CLOUDFLARE-VLESS-WS-424MS` (url=1118ms, status=HTTP 204)
17. `AKUN-027-CLOUDFLARE-VLESS-WS-499MS` (url=842ms, status=HTTP 204)
18. `AKUN-028-CLOUDFLARE-VLESS-WS-524MS` (url=2501ms, status=HTTP 204)
19. `AKUN-032-OPENAI-VLESS-WS-389MS` (url=997ms, status=HTTP 204)
20. `AKUN-033-CLOUDFLARE-VLESS-WS-608MS` (url=959ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
