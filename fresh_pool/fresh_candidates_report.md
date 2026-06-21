# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-CNAE-VLESS-WS-98MS` (url=243ms, nekobox=306ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-130MS` (url=287ms, nekobox=306ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-112MS` (url=275ms, nekobox=283ms, status=yes)
4. `AKUN-004-OPENAI-VLESS-WS-146MS` (url=291ms, nekobox=338ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-121MS` (url=257ms, nekobox=310ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-147MS` (url=314ms, nekobox=316ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-122MS` (url=448ms, nekobox=329ms, status=yes)
8. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-133MS` (url=264ms, nekobox=292ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-105MS` (url=291ms, nekobox=287ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-349MS` (url=763ms, nekobox=797ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-372MS` (url=750ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-331MS` (url=604ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-366MS` (url=764ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-302MS` (url=697ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-371MS` (url=742ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-318MS` (url=719ms, status=HTTP 204)
17. `AKUN-028-PUFFYSHOP-VLESS-WS-645MS` (url=859ms, status=HTTP 204)
18. `AKUN-029-CLOUDFLARE-VLESS-WS-592MS` (url=1053ms, status=HTTP 204)
19. `AKUN-031-PUFFYSHOP-VLESS-WS-755MS` (url=1155ms, status=HTTP 204)
20. `AKUN-033-CLOUDFLARE-VLESS-WS-682MS` (url=1061ms, status=HTTP 204)
21. `AKUN-035-UNKNOWN-VLESS-WS-844MS` (url=3521ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
