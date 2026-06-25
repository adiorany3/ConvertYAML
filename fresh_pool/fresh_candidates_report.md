# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-ORACLE-VLESS-WS-69MS` (url=231ms, nekobox=266ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS` (url=253ms, nekobox=301ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-110MS` (url=269ms, nekobox=304ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-104MS` (url=269ms, nekobox=271ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS` (url=258ms, nekobox=267ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=281ms, nekobox=291ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-125MS` (url=235ms, nekobox=275ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS` (url=274ms, nekobox=276ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS` (url=245ms, nekobox=306ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-100MS`
11. `AKUN-012-UNKNOWN-VLESS-WS-279MS` (url=596ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-284MS` (url=616ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-299MS` (url=666ms, status=HTTP 204)
14. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-287MS` (url=657ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-311MS` (url=608ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-313MS` (url=637ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-288MS` (url=514ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-414MS` (url=719ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-321MS` (url=569ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-390MS` (url=727ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-133MS` (url=241ms, status=HTTP 204)
22. `AKUN-028-IETF-VLESS-WS-533MS` (url=887ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-518MS` (url=949ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-614MS` (url=1118ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
