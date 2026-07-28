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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=197ms, nekobox=230ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=221ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-141MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-108MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-167MS` (url=251ms, status=HTTP 204)
12. `AKUN-014-UNKNOWN-VLESS-WS-74MS` (url=223ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-175MS` (url=246ms, status=HTTP 204)
14. `AKUN-016-090227-VLESS-WS-147MS` (url=373ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-217MS` (url=419ms, status=HTTP 204)
16. `AKUN-021-UNKNOWN-VLESS-WS-276MS` (url=523ms, status=HTTP 204)
17. `AKUN-022-UNKNOWN-VLESS-WS-290MS` (url=527ms, status=HTTP 204)
18. `AKUN-023-UNKNOWN-VLESS-WS-262MS` (url=481ms, status=HTTP 204)
19. `AKUN-025-SUKARIO-VLESS-WS-403MS` (url=718ms, status=HTTP 204)
20. `AKUN-026-UNKNOWN-VLESS-WS-413MS` (url=456ms, status=HTTP 204)
21. `AKUN-027-UNKNOWN-VLESS-WS-389MS` (url=642ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-502MS` (url=1495ms, status=HTTP 204)
23. `AKUN-031-UNKNOWN-VLESS-WS-506MS` (url=821ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-563MS` (url=858ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-649MS` (url=1497ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
