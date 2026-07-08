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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=201ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=228ms, nekobox=227ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=208ms, nekobox=273ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=219ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=220ms, nekobox=245ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-73MS` (url=228ms, nekobox=242ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-70MS` (url=225ms, nekobox=229ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-71MS` (url=237ms, nekobox=251ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS` (url=239ms, nekobox=276ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-121MS` (url=205ms, nekobox=264ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-89MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-116MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-84MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-82MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-143MS` (url=220ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-162MS` (url=323ms, status=HTTP 204)
17. `AKUN-018-PUBLICDOMAINREGISTRY-NET-VLESS-WS-136MS` (url=250ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-71MS` (url=244ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-94MS` (url=250ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-366MS` (url=791ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-388MS` (url=864ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-403MS` (url=847ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-475MS` (url=1156ms, status=HTTP 204)
24. `AKUN-027-SPEEDTEST-VLESS-WS-392MS` (url=738ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-708MS` (url=1362ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
