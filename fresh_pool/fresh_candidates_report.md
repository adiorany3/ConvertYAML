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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-VULTR-VLESS-WS-65MS` (url=246ms, nekobox=257ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=258ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=256ms, nekobox=257ms, status=yes)
4. `AKUN-004-MYBB-VLESS-WS-82MS` (url=273ms, nekobox=275ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-101MS` (url=241ms, nekobox=260ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-84MS` (url=250ms, nekobox=267ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS` (url=238ms, nekobox=256ms, status=yes)
8. `AKUN-008-1PASSWORD-VLESS-WS-82MS` (url=240ms, nekobox=257ms, status=yes)
9. `AKUN-009-VULTR-VLESS-WS-78MS` (url=223ms, nekobox=256ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-121MS` (url=228ms, nekobox=257ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-97MS` (url=235ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-158MS` (url=263ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=240ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-262MS` (url=571ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-84MS` (url=288ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-291MS` (url=625ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-290MS` (url=616ms, status=HTTP 204)
19. `AKUN-020-SPEEDTEST-VLESS-WS-254MS` (url=569ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-79MS` (url=270ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-332MS` (url=817ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-314MS` (url=615ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-369MS` (url=631ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-79MS` (url=282ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-265MS` (url=567ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
