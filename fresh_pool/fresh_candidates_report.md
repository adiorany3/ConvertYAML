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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=210ms, nekobox=234ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-85MS` (url=227ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=226ms, nekobox=233ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-96MS` (url=231ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=216ms, nekobox=230ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=200ms, nekobox=291ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=225ms, nekobox=266ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-89MS` (url=211ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-107MS` (url=222ms, nekobox=238ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS` (url=204ms, nekobox=256ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-118MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-97MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-110MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS` (url=200ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-155MS` (url=591ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-137MS` (url=202ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-84MS` (url=200ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-131MS` (url=299ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-145MS` (url=385ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-182MS` (url=392ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-175MS` (url=311ms, status=HTTP 204)
22. `AKUN-022-ZVC-VLESS-WS-85MS` (url=201ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-367MS` (url=994ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-378MS` (url=861ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-372MS` (url=846ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
