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
1. `AKUN-001-EU-VLESS-WS-98MS` (url=238ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS` (url=284ms, nekobox=272ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS` (url=236ms, nekobox=276ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS` (url=245ms, nekobox=276ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-138MS` (url=245ms, nekobox=275ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-115MS` (url=247ms, nekobox=296ms, status=yes)
7. `AKUN-007-OPENAI-VLESS-WS-106MS` (url=236ms, nekobox=266ms, status=yes)
8. `AKUN-008-AMAZON-VLESS-WS-101MS` (url=230ms, nekobox=277ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-132MS` (url=245ms, nekobox=186ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS`
11. `AKUN-010-AMAZON-VLESS-WS-96MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-274MS` (url=565ms, status=HTTP 204)
13. `AKUN-013-CONFLU-VLESS-WS-269MS` (url=588ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-295MS` (url=623ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-312MS` (url=641ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-293MS` (url=5657ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-310MS` (url=649ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-317MS` (url=640ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-331MS` (url=4489ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-306MS` (url=2092ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-453MS` (url=637ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-71MS` (url=565ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-586MS` (url=1018ms, status=HTTP 204)
24. `AKUN-034-RS-RAPIDSEEDBOX-20190717-VLESS-WS-627MS` (url=951ms, status=HTTP 204)
25. `AKUN-035-RS-RAPIDSEEDBOX-20190717-VLESS-WS-650MS` (url=2851ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
