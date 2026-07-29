# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=212ms, nekobox=222ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=201ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS` (url=202ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=200ms, nekobox=223ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-69MS` (url=198ms, nekobox=229ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-113MS` (url=250ms, nekobox=249ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-58MS` (url=200ms, nekobox=231ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-89MS` (url=212ms, nekobox=245ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-58MS` (url=199ms, nekobox=242ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-64MS` (url=209ms, nekobox=240ms, status=yes)
11. `AKUN-011-OPENAI-VLESS-WS-105MS` (url=203ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-105MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-132MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-140MS` (url=283ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-105MS` (url=645ms, status=HTTP 204)
16. `AKUN-016-RMGYVPN-VLESS-WS-119MS` (url=403ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-162MS` (url=228ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=229ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-216MS` (url=490ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-237MS` (url=2452ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-121MS` (url=211ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-394MS` (url=652ms, status=HTTP 204)
23. `AKUN-027-ZABIDAT-VLESS-WS-466MS` (url=889ms, status=HTTP 204)
24. `AKUN-028-DEV-VLESS-WS-98MS` (url=999ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-510MS` (url=837ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
