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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=210ms, nekobox=247ms, status=yes)
2. `AKUN-002-VULTR-VLESS-WS-72MS` (url=217ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=232ms, nekobox=282ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=211ms, nekobox=248ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS` (url=198ms, nekobox=240ms, status=yes)
6. `AKUN-006-US-VLESS-WS-103MS` (url=309ms, nekobox=252ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-76MS` (url=195ms, nekobox=244ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS` (url=216ms, nekobox=240ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-121MS` (url=215ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS` (url=226ms, nekobox=237ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-114MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-79MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-117MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-232MS` (url=493ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-230MS` (url=508ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-266MS` (url=570ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-264MS` (url=563ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-270MS` (url=567ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-276MS` (url=484ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-293MS` (url=563ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-276MS` (url=612ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-328MS` (url=545ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-348MS` (url=466ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-423MS` (url=690ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-510MS` (url=827ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
