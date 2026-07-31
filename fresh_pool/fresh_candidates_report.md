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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=208ms, nekobox=226ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=220ms, nekobox=241ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-65MS` (url=199ms, nekobox=221ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-58MS` (url=198ms, nekobox=223ms, status=yes)
5. `AKUN-005-OPENAI-VLESS-WS-63MS` (url=226ms, nekobox=227ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-57MS` (url=201ms, nekobox=229ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-67MS` (url=209ms, nekobox=225ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-77MS` (url=201ms, nekobox=224ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-59MS` (url=203ms, nekobox=238ms, status=yes)
10. `AKUN-010-SPEEDTEST-VLESS-WS-82MS` (url=213ms, nekobox=184ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS`
12. `AKUN-012-008500-VLESS-WS-82MS` (url=198ms, status=HTTP 204)
13. `AKUN-013-SPEEDTEST-VLESS-WS-66MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-SPEEDTEST-VLESS-WS-69MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-70MS` (url=200ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-62MS` (url=197ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-164MS` (url=278ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-124MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-NET-141-11-202-0-23-VLESS-WS-225MS` (url=487ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-396MS` (url=656ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-316MS` (url=713ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-446MS` (url=760ms, status=HTTP 204)
23. `AKUN-027-PLAY2GO-CUSTOMERS-NETWOR-VLESS-WS-445MS` (url=1644ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-421MS` (url=1198ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-537MS` (url=822ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
