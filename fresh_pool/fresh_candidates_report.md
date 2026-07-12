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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=249ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=204ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=216ms, nekobox=258ms, status=yes)
4. `AKUN-004-IONOS-VLESS-WS-84MS` (url=215ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=205ms, nekobox=242ms, status=yes)
6. `AKUN-006-BROADNNET-KR-VLESS-WS-98MS` (url=237ms, nekobox=267ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-95MS` (url=227ms, nekobox=230ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS` (url=229ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-104MS` (url=227ms, nekobox=230ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-115MS` (url=246ms, nekobox=231ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-92MS` (url=201ms, status=HTTP 204)
12. `AKUN-012-ALIBABA-VLESS-WS-109MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-118MS` (url=211ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-92MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-121MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-99MS` (url=230ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-129MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-US-VLESS-WS-108MS` (url=284ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-93MS` (url=203ms, status=HTTP 204)
20. `AKUN-020-PUBLICDOMAINREGISTRY-NET-VLESS-WS-132MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-98MS` (url=216ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-249MS` (url=521ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-253MS` (url=528ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-257MS` (url=586ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-271MS` (url=1650ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
